import connexion
import six

from swagger_server.models.googlerpc_status import GooglerpcStatus  # noqa: E501
from swagger_server.models.v1_create_process_metadata_request import V1CreateProcessMetadataRequest  # noqa: E501
from swagger_server.models.v1_create_process_metadata_response import V1CreateProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_create_process_report_request import V1CreateProcessReportRequest  # noqa: E501
from swagger_server.models.v1_create_process_report_response import V1CreateProcessReportResponse  # noqa: E501
from swagger_server.models.v1_generate_report_from_process_metadata_response import V1GenerateReportFromProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_get_process_metadata_response import V1GetProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_get_process_report_response import V1GetProcessReportResponse  # noqa: E501
from swagger_server.models.v1_list_process_metadata_response import V1ListProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_update_process_metadata_request import V1UpdateProcessMetadataRequest  # noqa: E501
from swagger_server.models.v1_update_process_metadata_response import V1UpdateProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_report_generation_status import V1ReportGenerationStatus
from swagger_server.models.v1_process_report_generation_status import V1ProcessReportGenerationStatus
from swagger_server.models.v1_process_insights import V1ProcessInsights
from swagger_server.models.v1_process_anchors import V1ProcessAnchors
from swagger_server.models.v1_process_metadata import V1ProcessAnchors, V1ProcessMetadata
from swagger_server.models.v1_process_report import V1ProcessMap, V1ProcessReport
from swagger_server import util
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
now = datetime.now()

processMap = """{
eyal_asulin: { data: { groupId: "R&D" } },
shay_nehmad: { data: { groupId: "R&D" } },
noa_bergman: { data: { groupId: "HR" } },
tal_shapira: { data: { groupId: "Founders-IL" } },
gal_nakash: { data: { groupId: "Founders-IL" } },
ofer_klein: { data: { groupId: "Founders-US" } },
external_1_1: { data: { groupId: "boldstart.vc", groupType: "external" } },
external_1_2: { data: { groupId: "boldstart.vc", groupType: "external" } },
external_2_1: { data: { groupId: "angularventures.com", groupType: "external" } },
external_2_2: { data: { groupId: "angularventures.com", groupType: "external" } },
l_rtm_1: {
    id1: "shay_nehmad",
    id2: "tal_shapira",
    glyphs: [ { image: "images/google-drive.svg" }, { image: "images/gmail.svg" } ],
},
l_rtm_2: {
    id1: "shay_nehmad",
    id2: "gal_nakash",
    glyphs: [ { image: "images/gmail.svg" } ],
},
l_rtm_3: {
    id1: "noa_bergman",
    id2: "ofer_klein",
    glyphs: [ { image: "images/gmail.svg" } ],
},
l_rtm_4: {
    id1: "noa_bergman",
    id2: "tal_shapira",
    glyphs: [ { image: "images/gmail.svg" } ],
},
l_rtm_5: {
    id1: "eyal_asulin",
    id2: "tal_shapira",
    glyphs: [ { image: "images/google-drive.svg" } ],
},
l_mtl_1: {
    id1: "tal_shapira",
    id2: "external_1_1",
    glyphs: [ { image: "images/gmail.svg", backgroundColor: "white", color: "white" } ],
},
l_mtl_2: {
    id1: "ofer_klein",
    id2: "external_1_2",
    glyphs: [ { image: "images/google-drive.svg", backgroundColor: "white", color: "white" } ],
},
l_mtl_3: {
    id1: "ofer_klein",
    id2: "external_2_1",
    glyphs: [ { image: "images/google-drive.svg", backgroundColor: "white" , color: "white"} ],
},
l_mtl_4: {
    id1: "ofer_klein",
    id2: "external_2_2",
    glyphs: [ { image: "images/gmail.svg", backgroundColor: "white" , color: "white"} ],
},
l_mtl_5: {
    id1: "gal_nakash",
    id2: "external_2_1",
    glyphs: [ { image: "images/google-drive.svg", backgroundColor: "white", color: "white" } ],
}
}"""

icon_url = "https://i.imgur.com/GptSzgL.png"
processMetadataList = [
    V1ProcessMetadata(
        id="1",
        name="Finance",
        description="FinanceTeam",
        icon_url=icon_url,
        anchors=V1ProcessAnchors(
            teams="Finance_legal, Finance_purchases"
        )
    ),
    V1ProcessMetadata(
        id="2",
        name="Procurement",
        description="ProcurementTeam",
        icon_url=icon_url,
        anchors=V1ProcessAnchors(
            teams="Procurement_europe, Procurement_usa"
        ),
    ),
    V1ProcessMetadata(
        id="3",
        name="RND",
        description="RndTeam",
        icon_url=icon_url,
        anchors=V1ProcessAnchors(
            teams="Rnd_dev, Rnd_qa, Rnd_infra"
        ),
    ),
]

processStatusList = [
    V1ProcessReportGenerationStatus(
        process_id="1",
        status=V1ReportGenerationStatus.DONE,
        time_remaining="0"
    ),
    V1ProcessReportGenerationStatus(
        process_id="2",
        status=V1ReportGenerationStatus.IN_PROGRESS,
        time_remaining="00:20:23"
    ),
    V1ProcessReportGenerationStatus(
        process_id="3",
        status=V1ReportGenerationStatus.UNSPECIFIED,
        time_remaining="0"
    ),
]

processReport = V1ProcessReport(
    process_id="1",
    map=V1ProcessMap(
        process_map=processMap,
    ),
    insights=V1ProcessInsights(
        business_owners="Tal, Gal",
        internal_users_count=3,
        external_users_count=2,
        external_domains_count=1,
        last_extraction=now,
        last_activity=datetime.now(),
    ),
    generated_for="Analyst",
    generated_at=datetime.now(),
)


def process_service_create_process_metadata(body):  # noqa: E501
    """Create new process metadata. Called from UI when pressing &#x27;+ Create new process&#x27; and manually by Analysts.

    create a new metadata object to be describe a process and use to generate and display the report. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: V1CreateProcessMetadataResponse
    """
    if connexion.request.is_json:
        body = V1CreateProcessMetadataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    new_metadata = body.md
    print(f"{new_metadata = }, before adding we have {len(processMetadataList)} items in the md DB")
    processMetadataList.append(new_metadata)
    resp = V1CreateProcessMetadataResponse(created_md=body.md)
    print(f"we now have {len(processMetadataList)} items in the md DB")
    print(f"returning {resp}, type {type(resp)}")
    return resp


def process_service_create_process_report(body):  # noqa: E501
    """Create a process report. If there is an existing report for the process, the existing reports will remain in the DB (for a while) if you want to revert.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: V1CreateProcessReportResponse
    """
    if connexion.request.is_json:
        body = V1CreateProcessReportRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def process_service_generate_report_from_process_metadata(process_id):  # noqa: E501
    """Trigger Argo workflow that generates a report from existing metadata.

    Sets up the proper Argo Workflow arguments and run the steps. # noqa: E501

    :param process_id: 
    :type process_id: str

    :rtype: V1GenerateReportFromProcessMetadataResponse
    """
    return 'do some magic!'


def process_service_get_process_metadata(process_metadata_id):  # noqa: E501
    """Return a process metadata, if exists.

    Called from the process generation flow or manually by analyst to get require details. # noqa: E501

    :param process_metadata_id: 
    :type process_metadata_id: str

    :rtype: V1GetProcessMetadataResponse
    """
    md = processMetadataList[0]
    md.id = process_metadata_id
    return V1GetProcessMetadataResponse(md=md)


def process_service_get_process_report(process_id):  # noqa: E501
    """Get a single process report.

    To use, you can fill just the ID. # noqa: E501

    :param process_id: 
    :type process_id: str

    :rtype: V1GetProcessReportResponse
    """
    return V1GetProcessReportResponse(report=processReport)


def process_service_list_process_metadata(limit=None):  # noqa: E501
    """List all process metadata (used from process lib screen).

    Called by UI/Analyst to display all processes metadata. # noqa: E501

    :param limit: 
    :type limit: int

    :rtype: V1ListProcessMetadataResponse
    """
    return V1ListProcessMetadataResponse(mds=processMetadataList, report_status=processStatusList)


def process_service_update_process_metadata(body):  # noqa: E501
    """Update an existing process metadata.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: V1UpdateProcessMetadataResponse
    """
    if connexion.request.is_json:
        body = V1UpdateProcessMetadataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
