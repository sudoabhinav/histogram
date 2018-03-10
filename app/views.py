import csv

from django.conf import settings
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """docstring for HomeView."""

    template_name = "app/home.html"

    def _get_data(self):
        data = dict()
        try:
            with open(settings.CSV_FILE_PATH) as infile:
                reader_obj = csv.reader(infile)
                data['headers'] = next(reader_obj)[:2]
                data['data'] = list()

                for line in reader_obj:
                    data['data'].append([int(line[0]), int(line[1])])

                # data['data'] = data['data'].sort(key=lambda x: x[0], reverse=True)
        except IOError:
            data['error'] = "Unable to parse csv file, please check the file!"
        except Exception:
            data['error'] = "Unknown error, please check csv file!"

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self._get_data()
        return context
