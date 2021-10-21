import json

from django.core.management import call_command
from django.test import TestCase

from experimenter.experiments.models import NimbusFeatureConfig
from experimenter.features import Features
from experimenter.features.tests import mock_valid_features


@mock_valid_features
class TestLoadFeatureConfigs(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Features.clear_cache()

    def test_load_feature_configs(self):
        self.assertFalse(NimbusFeatureConfig.objects.filter(slug="readerMode").exists())
        call_command("load_feature_configs")

        feature_config = NimbusFeatureConfig.objects.get(slug="readerMode")
        self.assertEqual(feature_config.name, "readerMode")
        self.assertEqual(
            feature_config.description,
            "Firefox Reader Mode",
        )
        self.assertEqual(
            json.loads(feature_config.schema),
            {
                "additionalProperties": True,
                "properties": {
                    "pocketCTAVersion": {
                        "description": (
                            "What version of Pocket "
                            "CTA to show in Reader "
                            "Mode (Empty string is no "
                            "CTA)"
                        ),
                        "type": "string",
                        "enum": ["v1", "v2"],
                    }
                },
                "type": "object",
            },
        )