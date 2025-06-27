#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2025.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------
from typing import Literal, Any

from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.gateway.providers import Providers
from ibm_watsonx_ai.gateway.models import Models
from ibm_watsonx_ai.wml_client_error import InvalidMultipleArguments, WMLClientError
from ibm_watsonx_ai.wml_resource import WMLResource


class Gateway(WMLResource):
    """Model Gateway class."""

    def __init__(
        self,
        *,
        credentials: Credentials | None = None,
        verify: bool | str | None = None,
        api_client: APIClient | None = None,
    ):
        if credentials:
            api_client = APIClient(credentials, verify=verify)
        elif not api_client:
            raise InvalidMultipleArguments(
                params_names_list=["credentials", "api_client"],
                reason="None of the arguments were provided.",
            )

        WMLResource.__init__(self, __name__, api_client)

        if self._client.ICP_PLATFORM_SPACES:
            raise WMLClientError("AI Gateway is not supported on CPD.")

        self.providers = Providers(self._client)
        self.models = Models(self._client)

        # Chat completions
        class _ChatCompletions(WMLResource):
            def __init__(self, api_client: APIClient):
                WMLResource.__init__(self, __name__, api_client)

            def create(self, model: str, messages: list[dict], **kwargs: Any) -> dict:
                """Generate chat completions for given model and messages.

                :param model: name of model for given provider or alias
                :type model: str

                :param messages: messages to be processed during call
                :type messages: list[dict]

                :returns: model answer
                :rtype: dict
                """
                request_json = {"messages": messages, "model": model}

                if kwargs:
                    request_json.update(**kwargs)

                response = self._client.httpx_client.post(
                    self._client._href_definitions.get_gateway_chat_completions_href(),
                    headers=self._client._get_headers(),
                    json=request_json,
                )

                return self._handle_response(200, "chat completion creation", response)

            async def acreate(
                self, model: str, messages: list[dict], **kwargs: Any
            ) -> dict:
                """Generate asynchronously chat completions for given model and messages.

                :param model: name of model for given provider or alias
                :type model: str

                :param messages: messages to be processed during call
                :type messages: list[dict]

                :returns: model answer
                :rtype: dict
                """
                request_json = {"messages": messages, "model": model}

                if kwargs:
                    request_json.update(**kwargs)

                response = await self._client.async_httpx_client.post(
                    self._client._href_definitions.get_gateway_chat_completions_href(),
                    headers=self._client._get_headers(),
                    json=request_json,
                )

                return self._handle_response(200, "chat completion creation", response)

        class _Chat:
            def __init__(self, api_client: APIClient):
                self.completions = _ChatCompletions(api_client)

        self.chat = _Chat(self._client)

        # Text completions
        class _Completions(WMLResource):
            def __init__(self, api_client: APIClient):
                WMLResource.__init__(self, __name__, api_client)

            def create(
                self, model: str, prompt: str | list[str] | list[int], **kwargs: Any
            ) -> dict:
                """Generate text completions for given model and prompt.

                :param model: name of model for given provider or alias
                :type model: str

                :param prompt: prompt for processing
                :type prompt: str or list[str] or list[int]

                :returns: model answer
                :rtype: dict
                """
                request_json = {"prompt": prompt, "model": model}

                if kwargs:
                    request_json.update(**kwargs)

                response = self._client.httpx_client.post(
                    self._client._href_definitions.get_gateway_text_completions_href(),
                    headers=self._client._get_headers(),
                    json=request_json,
                )

                return self._handle_response(200, "text completion creation", response)

            async def acreate(
                self, model: str, prompt: str | list[str] | list[int], **kwargs: Any
            ) -> dict:
                """Generate asynchronous text completions for given model and prompt.

                :param model: name of model for given provider or alias
                :type model: str

                :param prompt: prompt for processing
                :type prompt: str or list[str] or list[int]

                :returns: model answer
                :rtype: dict
                """
                request_json = {"prompt": prompt, "model": model}

                if kwargs:
                    request_json.update(**kwargs)

                response = await self._client.async_httpx_client.post(
                    self._client._href_definitions.get_gateway_text_completions_href(),
                    headers=self._client._get_headers(),
                    json=request_json,
                )

                return self._handle_response(200, "text completion creation", response)

        self.completions = _Completions(self._client)

        # Embeddings
        class _Embeddings(WMLResource):
            def __init__(self, api_client: APIClient):
                WMLResource.__init__(self, __name__, api_client)

            def create(
                self, model: str, input: str | list[str] | list[int], **kwargs: Any
            ) -> dict:
                """Generate embeddings for given model and input.

                :param model: name of model for given provider or alias
                :type model: str

                :param input: prompt for processing
                :type input: str or list[str] or list[int]

                :returns: embeddings for given model and input
                :rtype: dict
                """
                request_json = {"input": input, "model": model}

                if kwargs:
                    request_json.update(**kwargs)

                response = self._client.httpx_client.post(
                    self._client._href_definitions.get_gateway_embeddings_href(),
                    headers=self._client._get_headers(),
                    json=request_json,
                )

                return self._handle_response(200, "embedding creation", response)

            async def acreate(
                self, model: str, input: str | list[str] | list[int], **kwargs: Any
            ) -> dict:
                """Generate asynchronous embeddings for given model and input.

                :param model: name of model for given provider or alias
                :type model: str

                :param input: prompt for processing
                :type input: str or list[str] or list[int]

                :returns: embeddings for given model and input
                :rtype: dict
                """
                request_json = {"input": input, "model": model}

                if kwargs:
                    request_json.update(**kwargs)

                response = await self._client.async_httpx_client.post(
                    self._client._href_definitions.get_gateway_embeddings_href(),
                    headers=self._client._get_headers(),
                    json=request_json,
                )

                return self._handle_response(200, "embedding creation", response)

        self.embeddings = _Embeddings(self._client)

    def set_secrets_manager(
        self, secrets_manager: str, name: str = "Watsonx AI Model Gateway configuration"
    ) -> dict:
        """Configure Model Gateway by, among others, setting Secrets Manager url.

        :param secrets_manager: Secrets Manager url
        :type secrets_manager: str

        :param name: Model Gateway configuration name
        :type name: str, optional
        """
        response = self._client.httpx_client.post(
            self._client._href_definitions.get_gateway_tenant_href(),
            headers=self._client._get_headers(),
            json={"name": name, "secrets_manager": secrets_manager},
        )

        return self._handle_response(201, "set secrets manager", response)

    def clear_secrets_manager(self) -> str:
        """Clear Model Gateway configuration.

        :return: status ("SUCCESS" if succeeded)
        :rtype: str
        """
        response = self._client.httpx_client.delete(
            self._client._href_definitions.get_gateway_tenant_href(),
            headers=self._client._get_headers(),
        )

        return self._handle_response(
            204, "tenant deletion", response, json_response=False
        )
