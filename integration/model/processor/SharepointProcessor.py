from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.client_context import ClientCredential
import os


def print_download_progress(offset):
    print("Downloaded '{0}' bytes...".format(offset))


def download_from_sharepoint(url, client_id, secret_name, file_url, target_path):
    client_credentials = ClientCredential(client_id, secret_name)
    ctx = ClientContext(url).with_credentials(client_credentials)
    #file_url = '/sites/team/Shared Documents/big_buck_bunny.mp4'
    source_file = ctx.web.get_file_by_server_relative_url(file_url)
    local_file_name = os.path.join(target_path, os.path.basename(file_url))
    with open(local_file_name, "wb") as local_file:
        source_file.download_session(local_file, print_download_progress).execute_query()

    print("[Ok] file has been downloaded: {0}".format(local_file_name))


def upload_file_to_sharepoint(url, client_id, secret_name, target_url, source_path):
    #target_url = "/sites/team/Shared Documents"
    client_credentials = ClientCredential(client_id, secret_name)
    ctx = ClientContext(url).with_credentials(client_credentials)
    target_folder = ctx.web.get_folder_by_server_relative_url(target_url)
    size_chunk = 1000000
    #local_path = "../../../tests/data/big_buck_bunny.mp4"
    # local_path = "../../../tests/data/SharePoint User Guide.docx"

    file_size = os.path.getsize(source_path)

    def print_upload_progress(offset):
        print("Uploaded '{0}' bytes from '{1}'...[{2}%]".format(offset, file_size, round(offset / file_size * 100, 2)))

    uploaded_file = target_folder.files.create_upload_session(source_path, size_chunk,
                                                              print_upload_progress).execute_query()
    print('File {0} has been uploaded successfully'.format(uploaded_file.serverRelativeUrl))
