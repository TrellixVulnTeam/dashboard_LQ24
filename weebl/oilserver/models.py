import os
import utils
from django.db import models
from django.contrib.sites.models import Site


class WeeblSetting(models.Model):
    """Settings for Weebl"""
    site = models.OneToOneField(
        Site,
        unique=True,
        help_text="To make sure there is only ever one instance per website.")
    check_in_unstable_threshold = models.IntegerField(
        default=300,
        help_text="The time (sec) taken for jenkins to check in, problem \
        suspected if over.")
    check_in_down_threshold = models.IntegerField(
        default=1800,
        help_text="The time (sec) taken for jenkins to check in, definate \
        problem if over.")
    low_build_queue_threshold = models.IntegerField(
        default=3,
        help_text="There are too few builds in queue when lower than this.")
    overall_unstable_th = models.IntegerField(
        default=65,
        help_text="Overall success rate unstable thresholds.")
    overall_down_th = models.IntegerField(
        default=50,
        help_text="Overall success rate down thresholds.")
    down_colour = models.CharField(
        max_length=25,
        default="red",
        help_text="Highlight when warning.")
    unstable_colour = models.CharField(
        max_length=25,
        default="orange",
        help_text="Highlight when unstable.")
    up_colour = models.CharField(
        max_length=25,
        default="green",
        help_text="Highlight when no problems (up).")
    weebl_documentation = models.URLField(
        default=None,
        blank=True,
        help_text="URL to documentation.")

    def __str__(self):
        return str(self.site)


class Environment(models.Model):
    """The environment (e.g. Prodstack, Staging)."""
    uuid = models.CharField(
        max_length=36,
        default=utils.generate_uuid,
        unique=True,
        blank=False,
        null=False,
        help_text="UUID of environment")
    name = models.CharField(
        max_length=255,
        unique=True,
        default=uuid.default,
        blank=True,
        null=True,
        help_text="Name of environment")

    def __str__(self):
        return self.name


class ServiceStatus(models.Model):
    """Potential states that the CI server (Jenkins) may be in (e.g. up,
    unstable, down, unknown).
    """
    name = models.CharField(
        max_length=255,
        unique=True,
        default="Unknown",
        help_text="Current state of the environment.")
    description = models.TextField(
        default=None,
        blank=True,
        null=True,
        help_text="Optional description for status.")

    def __str__(self):
        return self.name


class Jenkins(models.Model):
    """The Continuous Integration Server."""
    environment = models.ForeignKey(Environment)
    service_status = models.ForeignKey(ServiceStatus)
    external_access_url = models.URLField(
        unique=True,
        help_text="A URL for external access to this server.")
    internal_access_url = models.URLField(
        default=None,
        blank=True,
        unique=True,
        help_text="A URL used internally (e.g. behind a firewall) for access \
        to this server.")
    service_status_updated_at = models.DateTimeField(
        default=utils.time_now(),
        blank=True,
        null=True,
        help_text="DateTime the service status was last updated.")

    def __str__(self):
        return self.external_access_url
