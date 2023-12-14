# Copyright 2023 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from taipy.gui import Markdown, notify

from .data_node_management import manage_partial


def notify_on_submission(state, submitable, details):
    if details["submission_status"] == "COMPLETED":
        notify(state, "success", "Submission completed!")
    elif details["submission_status"] == "FAILED":
        notify(state, "error", "Submission failed!")
    else:
        notify(state, "info", "In progress...")


def manage_data_node_partial(state):
    manage_partial(state)


scenario_page = Markdown("pages/scenario_page/scenario_page.md")