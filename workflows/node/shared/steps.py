# Copyright 2019-2023 SURF.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pydantic_forms.types import State
from orchestrator.workflow import step

from products.product_types.node import NodeProvisioning
from products.services.netbox.netbox import build_payload
from services import netbox


@step("Update node in IMS")
def update_node_in_ims(subscription: NodeProvisioning) -> State:
    """Update node in IMDB"""
    payload = build_payload(subscription.node, subscription)
    netbox.update(payload, id=subscription.node.ims_id)
    return {"subscription": subscription, "payload": payload.dict()}
