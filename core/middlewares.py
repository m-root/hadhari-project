from core.models import Organisation

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
import logging


logger = logging.getLogger('prj')


class OrganisationFromSubDomainMiddleware(MiddlewareMixin):
    """Middleware class that retrieves the current organisation from the sub-domain.
    """
    def process_request(self, request):
        """
        """
        domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
        pieces = domain.split('.')
        sub_domain = ".".join(pieces[:-2]) # join all but primary domain

        logger.info(sub_domain)

        try:
            organisation = Organisation.objects.get(id=sub_domain)
            logger.info(organisation)
            request.organisation = organisation

        except Organisation.DoesNotExist:
            request.organisation = None

        return
