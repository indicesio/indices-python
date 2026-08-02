# Tasks

Types:

```python
from indices.types import (
    SecretSlotDefinition,
    Task,
    TaskCreation,
    TaskFailureInfo,
    TaskListResponse,
    TaskDeleteResponse,
)
```

Methods:

- <code title="post /v1beta/tasks">client.tasks.<a href="./src/indices/resources/tasks.py">create</a>(\*\*<a href="src/indices/types/task_create_params.py">params</a>) -> <a href="./src/indices/types/task.py">Task</a></code>
- <code title="get /v1beta/tasks/{id}">client.tasks.<a href="./src/indices/resources/tasks.py">retrieve</a>(id) -> <a href="./src/indices/types/task.py">Task</a></code>
- <code title="get /v1beta/tasks">client.tasks.<a href="./src/indices/resources/tasks.py">list</a>() -> <a href="./src/indices/types/task_list_response.py">TaskListResponse</a></code>
- <code title="delete /v1beta/tasks/{id}">client.tasks.<a href="./src/indices/resources/tasks.py">delete</a>(id) -> <a href="./src/indices/types/task_delete_response.py">TaskDeleteResponse</a></code>
- <code title="post /v1beta/tasks/{id}/attach_capture_session">client.tasks.<a href="./src/indices/resources/tasks.py">attach_capture_session</a>(id, \*\*<a href="src/indices/types/task_attach_capture_session_params.py">params</a>) -> <a href="./src/indices/types/task.py">Task</a></code>

# Runs

Types:

```python
from indices.types import Run, RunLogsResponse
```

Methods:

- <code title="get /v1beta/runs/{run_id}">client.runs.<a href="./src/indices/resources/runs.py">retrieve</a>(run_id) -> <a href="./src/indices/types/run.py">Run</a></code>
- <code title="get /v1beta/runs">client.runs.<a href="./src/indices/resources/runs.py">list</a>(\*\*<a href="src/indices/types/run_list_params.py">params</a>) -> <a href="./src/indices/types/run.py">SyncCursorPage[Run]</a></code>
- <code title="get /v1beta/runs/{run_id}/logs">client.runs.<a href="./src/indices/resources/runs.py">logs</a>(run_id) -> <a href="./src/indices/types/run_logs_response.py">RunLogsResponse</a></code>
- <code title="post /v1beta/runs">client.runs.<a href="./src/indices/resources/runs.py">run</a>(\*\*<a href="src/indices/types/run_run_params.py">params</a>) -> <a href="./src/indices/types/run.py">Run</a></code>

# Secrets

Types:

```python
from indices.types import Secret, SecretListResponse, SecretDeleteResponse, SecretGetTotpResponse
```

Methods:

- <code title="post /v1beta/secrets">client.secrets.<a href="./src/indices/resources/secrets.py">create</a>(\*\*<a href="src/indices/types/secret_create_params.py">params</a>) -> <a href="./src/indices/types/secret.py">Secret</a></code>
- <code title="get /v1beta/secrets">client.secrets.<a href="./src/indices/resources/secrets.py">list</a>() -> <a href="./src/indices/types/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /v1beta/secrets/{id}">client.secrets.<a href="./src/indices/resources/secrets.py">delete</a>(id) -> <a href="./src/indices/types/secret_delete_response.py">SecretDeleteResponse</a></code>
- <code title="post /v1beta/secrets/{id}/totp">client.secrets.<a href="./src/indices/resources/secrets.py">get_totp</a>(id) -> <a href="./src/indices/types/secret_get_totp_response.py">SecretGetTotpResponse</a></code>

# Files

Types:

```python
from indices.types import (
    File,
    FileCreateResponse,
    FileDeleteResponse,
    FileFinalizeResponse,
    FileGetDownloadURLResponse,
)
```

Methods:

- <code title="post /v1beta/files">client.files.<a href="./src/indices/resources/files.py">create</a>(\*\*<a href="src/indices/types/file_create_params.py">params</a>) -> <a href="./src/indices/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /v1beta/files/{file_id}">client.files.<a href="./src/indices/resources/files.py">retrieve</a>(file_id) -> <a href="./src/indices/types/file.py">File</a></code>
- <code title="get /v1beta/files">client.files.<a href="./src/indices/resources/files.py">list</a>(\*\*<a href="src/indices/types/file_list_params.py">params</a>) -> <a href="./src/indices/types/file.py">SyncCursorPage[File]</a></code>
- <code title="delete /v1beta/files/{file_id}">client.files.<a href="./src/indices/resources/files.py">delete</a>(file_id) -> <a href="./src/indices/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1beta/files/{file_id}/download">client.files.<a href="./src/indices/resources/files.py">download</a>(file_id) -> None</code>
- <code title="post /v1beta/files/{file_id}/complete">client.files.<a href="./src/indices/resources/files.py">finalize</a>(file_id) -> <a href="./src/indices/types/file_finalize_response.py">FileFinalizeResponse</a></code>
- <code title="get /v1beta/files/{file_id}/download_url">client.files.<a href="./src/indices/resources/files.py">get_download_url</a>(file_id) -> <a href="./src/indices/types/file_get_download_url_response.py">FileGetDownloadURLResponse</a></code>

# CaptureSessions

Types:

```python
from indices.types import (
    CaptureSession,
    CaptureSessionState,
    SessionCookie,
    CaptureSessionListResponse,
)
```

Methods:

- <code title="post /v1beta/capture_sessions">client.capture_sessions.<a href="./src/indices/resources/capture_sessions.py">create</a>(\*\*<a href="src/indices/types/capture_session_create_params.py">params</a>) -> <a href="./src/indices/types/capture_session.py">CaptureSession</a></code>
- <code title="get /v1beta/capture_sessions/{id}">client.capture_sessions.<a href="./src/indices/resources/capture_sessions.py">retrieve</a>(id) -> <a href="./src/indices/types/capture_session.py">CaptureSession</a></code>
- <code title="get /v1beta/capture_sessions">client.capture_sessions.<a href="./src/indices/resources/capture_sessions.py">list</a>() -> <a href="./src/indices/types/capture_session_list_response.py">CaptureSessionListResponse</a></code>
- <code title="post /v1beta/capture_sessions/{id}/complete">client.capture_sessions.<a href="./src/indices/resources/capture_sessions.py">complete</a>(id) -> <a href="./src/indices/types/capture_session.py">CaptureSession</a></code>
