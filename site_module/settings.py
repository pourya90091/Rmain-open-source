from site_module.models import SiteSettings

base_url = SiteSettings.objects.get(main=True).base_url
site_email = SiteSettings.objects.get(main=True).email
protocol = 'https'
