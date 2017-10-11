import wmi

class VM():

    crt = wmi.WMI(namespace="root/virtualization/v2", find_classes=False)
    system_man = crt.Msvm_VirtualSystemManagementService()[0]

    def __init__(self,name):
        self.name = name

    def create_vm(self,vmname,cpu_number,mem_quantity):
        vcpu = self.crt.Msvm_ProcessorSettingData()[0]
        vcpu.VirtualQuantity = cpu_number
        vmem = self.crt.Msvm_MemorySettingData()[0]
        vmem.VirtualQuantity = mem_quantity
        vsettings = self.crt.Msvm_VirtualSystemSettingData()[0]
        vsettings.ElementName = vmname
        self.system_man.DefineSystem(ResourceSettings = [vcpu.GetText_(1), vmem.GetText_(1)], 
            ReferenceConfiguration = None, SystemSettings = vsettings.GetText_(1))

    def start_vm(self,vmname,state):
        state_change = self.crt.Msvm_ComputerSystem(ElementName = vmname)[0]
        state_change.RequestStateChange(RequestedState = state, TimeoutPeriod = None)

    def stop_vm(self,vmname,state):
        state_change = self.crt.Msvm_ComputerSystem(ElementName = vmname)[0]
        state_change.RequestStateChange(RequestedState = state, TimeoutPeriod = None)

    def distroy_vm(self,vmname):
        vm_system = self.crt.Msvm_ComputerSystem(ElementName = vmname)[0]
        self.system_man.DestroySystem(AffectedSystem = vm_system.path_())

if __name__ == '__main__':
    test = VM
    vmname = "TEESSTT123"
    cpu_number = 2
    mem_quantity = 2500
    state = 2
    #test.create_vm(VM,vmname,cpu_number,mem_quantity)
    #test.start_vm(VM,vmname,state)
    #test.stop_vm(VM,vmname,3)
    #test.distroy_vm(VM,vmname)