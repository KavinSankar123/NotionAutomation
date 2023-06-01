from CanvasEndpoint import CanvasEndpointClass
from NotionEndpoint import NotionEndpointClass

canvas_endpoint = CanvasEndpointClass()
notion_endpoint = NotionEndpointClass()

all_class_assignments = canvas_endpoint.get_assignments()

for i in range(len(all_class_assignments)):
    prepared_data = notion_endpoint.prepare_data(all_class_assignments[i])
    notion_endpoint.upload_assignment(prepared_data)
