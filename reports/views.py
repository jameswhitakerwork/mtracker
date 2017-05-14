from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from .models import Report
from .forms import ReportForm, ReportSubmitForm
from .filters import ReportFilter


import django_tables2 as tables
from django_tables2.utils import A


# Tables


class ReportTable(tables.Table):
    pos = tables.Column(accessor='report.report_name')
    link = tables.LinkColumn(
        'report_view',
        args=[A('pk')],
        orderable=True,
        text='View'
    )

    class Meta:
        model = Report
        fields = ['program', 'name', 'reportee', 'deadline', 'report']
        attrs = {'class': 'paleblue'}

# Views


class ReportCreate(SuccessMessageMixin, CreateView):
    form_class = ReportForm
    template_name = 'reports/form.html'
    success_url = '/reports/'
    success_message = '%(name)s was created successfully'

class ReportSubmit(UpdateView):
    model = Report
    form_class = ReportSubmitForm
    template_name = 'reports/form.html'
    success_url = '/reports/'

@login_required
def report_list(request):
    reports = Report.objects.all().order_by('deadline')
    table = ReportTable(reports)
    f = ReportFilter(request.GET, queryset=reports)
    return render(
        request,
        'reports/reports_list.html',
        {'table': table, 'reports': reports, 'f': f}
    )


def report_download(request, filename):
  path = os.expanduser('~/files/pdf/')
  wrapper = FileWrapper(file(filename,'rb'))
  response = HttpResponse(wrapper, content_type=mimetypes.guess_type(filename)[0])
  response['Content-Length'] = os.path.getsize(filename)
  response['Content-Disposition'] = "attachment; filename=" + filename
  return response

  reportdownload = permission_required('download_reports')(report_download)


def send_alerts(request):
        current_site = Site.objects.get_current()
        domain = current_site.domain
        for report in Report.objects.all():
            deadline = str(report.deadline)
            link = domain + '/reports/report-submit/%s' % report.id
            print report.reportee
            if not report.report:

                if report.days_left() == 14:
                    subject = "%s is due in 2 weeks" % report.name
                    print subject
                    message = "%s is due on %s. Go to %s to mark this report as submitted." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee],
                        cc="ssimpson@iom.int",
                        fail_silently=False
                    )

                if report.days_left() == 1:
                    subject = "%s is due tomorrow" % report.name
                    print subject
                    message = "%s is due on %s. Go to %s to mark this report as submitted." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee],
                        cc="ssimpson@iom.int",
                        fail_silently=False
                    )
                if report.days_left() < 0:
                    subject = "%s is overdue by %s days" % (report.name, str(-report.days_left()))
                    print subject
                    message = "%s was due on %s. Go to %s to submit this report." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee],
                        fail_silently=False,
                        cc="ssimpson@iom.int",
                    )