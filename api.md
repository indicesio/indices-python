# Beta

## Connectors

Types:

```python
from indices.types.beta import (
    Connector,
    SecretSlotDefinition,
    ConnectorDeleteResponse,
    ConnectorListRevisionsResponse,
)
```

Methods:

- <code title="get /v1beta/connectors/{connector_id}">client.beta.connectors.<a href="./src/indices/resources/beta/connectors.py">retrieve</a>(connector_id) -> <a href="./src/indices/types/beta/connector.py">Connector</a></code>
- <code title="get /v1beta/connectors">client.beta.connectors.<a href="./src/indices/resources/beta/connectors.py">list</a>(\*\*<a href="src/indices/types/beta/connector_list_params.py">params</a>) -> <a href="./src/indices/types/beta/connector.py">SyncCursorPage[Connector]</a></code>
- <code title="delete /v1beta/connectors/{connector_id}">client.beta.connectors.<a href="./src/indices/resources/beta/connectors.py">delete</a>(connector_id) -> <a href="./src/indices/types/beta/connector_delete_response.py">ConnectorDeleteResponse</a></code>
- <code title="get /v1beta/connectors/{connector_id}/revisions">client.beta.connectors.<a href="./src/indices/resources/beta/connectors.py">list_revisions</a>(connector_id) -> <a href="./src/indices/types/beta/connector_list_revisions_response.py">ConnectorListRevisionsResponse</a></code>

## Runs

Types:

```python
from indices.types.beta import Run, RunLogsResponse
```

Methods:

- <code title="get /v1beta/runs/{run_id}">client.beta.runs.<a href="./src/indices/resources/beta/runs.py">retrieve</a>(run_id) -> <a href="./src/indices/types/beta/run.py">Run</a></code>
- <code title="get /v1beta/runs">client.beta.runs.<a href="./src/indices/resources/beta/runs.py">list</a>(\*\*<a href="src/indices/types/beta/run_list_params.py">params</a>) -> <a href="./src/indices/types/beta/run.py">SyncCursorPage[Run]</a></code>
- <code title="get /v1beta/runs/{run_id}/logs">client.beta.runs.<a href="./src/indices/resources/beta/runs.py">logs</a>(run_id) -> <a href="./src/indices/types/beta/run_logs_response.py">RunLogsResponse</a></code>
- <code title="post /v1beta/runs">client.beta.runs.<a href="./src/indices/resources/beta/runs.py">run</a>(\*\*<a href="src/indices/types/beta/run_run_params.py">params</a>) -> <a href="./src/indices/types/beta/run.py">Run</a></code>

## Secrets

Types:

```python
from indices.types.beta import (
    Secret,
    SecretListResponse,
    SecretDeleteResponse,
    SecretGetTotpResponse,
)
```

Methods:

- <code title="post /v1beta/secrets">client.beta.secrets.<a href="./src/indices/resources/beta/secrets.py">create</a>(\*\*<a href="src/indices/types/beta/secret_create_params.py">params</a>) -> <a href="./src/indices/types/beta/secret.py">Secret</a></code>
- <code title="get /v1beta/secrets">client.beta.secrets.<a href="./src/indices/resources/beta/secrets.py">list</a>() -> <a href="./src/indices/types/beta/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /v1beta/secrets/{id}">client.beta.secrets.<a href="./src/indices/resources/beta/secrets.py">delete</a>(id) -> <a href="./src/indices/types/beta/secret_delete_response.py">SecretDeleteResponse</a></code>
- <code title="post /v1beta/secrets/{id}/totp">client.beta.secrets.<a href="./src/indices/resources/beta/secrets.py">get_totp</a>(id) -> <a href="./src/indices/types/beta/secret_get_totp_response.py">SecretGetTotpResponse</a></code>

## Files

Types:

```python
from indices.types.beta import (
    File,
    FileCreateResponse,
    FileDeleteResponse,
    FileFinalizeResponse,
    FileGetDownloadURLResponse,
)
```

Methods:

- <code title="post /v1beta/files">client.beta.files.<a href="./src/indices/resources/beta/files.py">create</a>(\*\*<a href="src/indices/types/beta/file_create_params.py">params</a>) -> <a href="./src/indices/types/beta/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /v1beta/files/{file_id}">client.beta.files.<a href="./src/indices/resources/beta/files.py">retrieve</a>(file_id) -> <a href="./src/indices/types/beta/file.py">File</a></code>
- <code title="get /v1beta/files">client.beta.files.<a href="./src/indices/resources/beta/files.py">list</a>(\*\*<a href="src/indices/types/beta/file_list_params.py">params</a>) -> <a href="./src/indices/types/beta/file.py">SyncCursorPage[File]</a></code>
- <code title="delete /v1beta/files/{file_id}">client.beta.files.<a href="./src/indices/resources/beta/files.py">delete</a>(file_id) -> <a href="./src/indices/types/beta/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1beta/files/{file_id}/download">client.beta.files.<a href="./src/indices/resources/beta/files.py">download</a>(file_id) -> None</code>
- <code title="post /v1beta/files/{file_id}/complete">client.beta.files.<a href="./src/indices/resources/beta/files.py">finalize</a>(file_id) -> <a href="./src/indices/types/beta/file_finalize_response.py">FileFinalizeResponse</a></code>
- <code title="get /v1beta/files/{file_id}/download_url">client.beta.files.<a href="./src/indices/resources/beta/files.py">get_download_url</a>(file_id) -> <a href="./src/indices/types/beta/file_get_download_url_response.py">FileGetDownloadURLResponse</a></code>

## CaptureSessions

Types:

```python
from indices.types.beta import (
    CaptureSession,
    CaptureSessionState,
    SessionCookie,
    CaptureSessionListResponse,
)
```

Methods:

- <code title="post /v1beta/capture_sessions">client.beta.capture_sessions.<a href="./src/indices/resources/beta/capture_sessions.py">create</a>(\*\*<a href="src/indices/types/beta/capture_session_create_params.py">params</a>) -> <a href="./src/indices/types/beta/capture_session.py">CaptureSession</a></code>
- <code title="get /v1beta/capture_sessions/{id}">client.beta.capture_sessions.<a href="./src/indices/resources/beta/capture_sessions.py">retrieve</a>(id) -> <a href="./src/indices/types/beta/capture_session.py">CaptureSession</a></code>
- <code title="get /v1beta/capture_sessions">client.beta.capture_sessions.<a href="./src/indices/resources/beta/capture_sessions.py">list</a>() -> <a href="./src/indices/types/beta/capture_session_list_response.py">CaptureSessionListResponse</a></code>
- <code title="post /v1beta/capture_sessions/{id}/abandon">client.beta.capture_sessions.<a href="./src/indices/resources/beta/capture_sessions.py">abandon</a>(id) -> <a href="./src/indices/types/beta/capture_session.py">CaptureSession</a></code>
- <code title="post /v1beta/capture_sessions/{id}/complete">client.beta.capture_sessions.<a href="./src/indices/resources/beta/capture_sessions.py">complete</a>(id) -> <a href="./src/indices/types/beta/capture_session.py">CaptureSession</a></code>
