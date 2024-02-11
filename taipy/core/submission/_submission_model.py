# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from sqlalchemy import JSON, Boolean, Column, Enum, String, Table

from .._repository._base_taipy_model import _BaseModel
from .._repository.db._sql_base_model import mapper_registry
from ..job.job_id import JobId
from .submission_status import SubmissionStatus


@mapper_registry.mapped
@dataclass
class _SubmissionModel(_BaseModel):
    __table__ = Table(
        "submission",
        mapper_registry.metadata,
        Column("id", String, primary_key=True),
        Column("entity_id", String),
        Column("entity_type", String),
        Column("entity_config_id", String),
        Column("job_ids", JSON),
        Column("properties", JSON),
        Column("creation_date", String),
        Column("submission_status", Enum(SubmissionStatus)),
        Column("version", String),
        Column("is_completed", Boolean),
        Column("is_abandoned", Boolean),
        Column("is_canceled", Boolean),
        Column("running_jobs", JSON),
        Column("blocked_jobs", JSON),
        Column("pending_jobs", JSON),
    )
    id: str
    entity_id: str
    entity_type: str
    entity_config_id: Optional[str]
    job_ids: Union[List[JobId], List]
    properties: Dict[str, Any]
    creation_date: str
    submission_status: SubmissionStatus
    version: str
    is_completed: bool
    is_abandoned: bool
    is_canceled: bool
    running_jobs: List[str]
    blocked_jobs: List[str]
    pending_jobs: List[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return _SubmissionModel(
            id=data["id"],
            entity_id=data["entity_id"],
            entity_type=data["entity_type"],
            entity_config_id=data.get("entity_config_id"),
            job_ids=_BaseModel._deserialize_attribute(data["job_ids"]),
            properties=_BaseModel._deserialize_attribute(data["properties"]),
            creation_date=data["creation_date"],
            submission_status=SubmissionStatus._from_repr(data["submission_status"]),
            version=data["version"],
            is_completed=data["is_completed"],
            is_abandoned=data["is_abandoned"],
            is_canceled=data["is_canceled"],
            running_jobs=_BaseModel._deserialize_attribute(data["running_jobs"]),
            blocked_jobs=_BaseModel._deserialize_attribute(data["blocked_jobs"]),
            pending_jobs=_BaseModel._deserialize_attribute(data["pending_jobs"]),
        )

    def to_list(self):
        return [
            self.id,
            self.entity_id,
            self.entity_type,
            self.entity_config_id,
            _BaseModel._serialize_attribute(self.job_ids),
            _BaseModel._serialize_attribute(self.properties),
            self.creation_date,
            repr(self.submission_status),
            self.version,
            self.is_completed,
            self.is_abandoned,
            self.is_canceled,
            _BaseModel._serialize_attribute(self.running_jobs),
            _BaseModel._serialize_attribute(self.blocked_jobs),
            _BaseModel._serialize_attribute(self.pending_jobs),
        ]