import json

from django.core.management import BaseCommand

from magazine.models import Autocar, Marka


class Command(BaseCommand):
    def handle(self, *args, **options):
        Marka.objects.all().delete()
        Autocar.objects.all().delete()

        with open('./data.json', 'r') as f:
            the_list = json.loads(f.read())

        marka_to_fill = []
        autocar_to_fill = []
        index_for_autocar = {}
        for item in the_list:
            if item['model'] == 'magazine.marka':
                temp = Marka(**item['fields'])
                marka_to_fill.append(temp)
                index_for_autocar |= ({item['pk']: temp})
            elif item['model'] == 'magazine.autocar':
                autocar_to_fill.append(Autocar(name=item['fields']['name'],
                                               description=item['fields']['description'],
                                               image=item['fields']['image'],
                                               price=item['fields']['price'],
                                               data_created=item['fields']['data_created'],
                                               marka=index_for_autocar[item['fields']['marka']]))

        Marka.objects.bulk_create(marka_to_fill)
        Autocar.objects.bulk_create(autocar_to_fill)