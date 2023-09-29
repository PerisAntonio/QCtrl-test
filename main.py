import fireopal
from qiskit_ibm_provider import IBMProvider

def run(input_data, solver_params, extra_arguments):
    provider=IBMProvider()
    account=provider.active_account()
    token=account['token']
    hub,group,project=account['instance'].split('/')
    credentials = fireopal.credentials.make_credentials_for_ibmq(token=token, hub=hub, group=group, project=project)
    supported_devices = fireopal.show_supported_devices(credentials=credentials)["supported_devices"]
    return supported_devices
