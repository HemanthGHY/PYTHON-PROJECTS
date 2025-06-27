#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2025.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------
from typing import Literal

import pandas as pd

from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.wml_resource import WMLResource


class Policies(WMLResource):
    """Model Gateway policies class."""

    def __init__(self, api_client: APIClient):
        WMLResource.__init__(self, __name__, api_client)

    def create(
        self, action: str, resource: str, subject: str, effect: str | None = None
    ) -> dict:
        """Create policy.

        :param action: action for policy
        :type action: str

        :param resource: resource for policy
        :type resource: str

        :param subject: subject for policy
        :type subject: str

        :param effect: effect for policy
        :type effect: str, optional

        :returns: policy details
        :rtype: dict
        """

        request_json = {"action": action, "resource": resource, "subject": subject}

        if effect:
            request_json["effect"] = effect

        response = self._client.httpx_client.post(
            self._client._href_definitions.get_gateway_policy_href(),
            headers=self._client._get_headers(),
            json=request_json,
        )

        return self._handle_response(204, "policy creation", response)

    def delete(
        self, action: str, resource: str, subject: str, effect: str | None = None
    ) -> str:
        """Delete policy.

        :param action: action for policy
        :type action: str

        :param resource: resource for policy
        :type resource: str

        :param subject: subject for policy
        :type subject: str

        :param effect: effect for policy
        :type effect: str, optional

        :returns: policy details
        :rtype: dict
        """
        request_json = {"action": action, "resource": resource, "subject": subject}

        if effect:
            request_json["effect"] = effect

        response = self._client.httpx_client.delete(
            self._client._href_definitions.get_gateway_policy_href(),
            headers=self._client._get_headers(),
            json=request_json,
        )

        return self._handle_response(
            204, "policy deletion", response, json_response=False
        )

    def get_details(self) -> dict:
        """Get policies details.

        :returns: policies details
        :rtype: dict
        """
        response = self._client.httpx_client.get(
            self._client._href_definitions.get_gateway_policy_href(),
            headers=self._client._get_headers(),
        )

        return self._handle_response(200, "policy listing", response)

    def list(self) -> pd.DataFrame:
        """List policies.

        :returns: dataframe with policies details
        :rtype: pandas.DataFrame
        """
        policy_details = self.get_details()

        policies_values = [
            (m["resource"], m["action"], m["subject"], m.get("effect", ""))
            for m in policy_details
        ]

        table = self._list(
            policies_values, ["RESOURCE", "ACTION", "SUBJECT", "EFFECT"], limit=None
        )

        return table
