pip install

from bdc_connect_sdk.auth import BdcConnectClient
from bdc_connect_sdk.auth import DatabricksClient
from bdc_connect_sdk.utils import csn_generator

bdc_connect_client = BdcConnectClient(DatabricksClient(dbutils, "<recipient-name>"))

share_name = "<share-name>"

csn_schema = csn_generator.generate_csn_template(share_name)

bdc_connect_client.create_or_update_share_csn(
    share_name,
    csn_schema
)