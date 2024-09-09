import time
from tvm.driver import tvmc
import numpy as np
import tvm
import warnings 
warnings.filterwarnings('ignore')
#Step 1: Load

def compile_onnx_to_tvm(onnx_file):
    model = tvmc.load(onnx_file)


    #Step 1.5: Optional Tune
    print("################# Logging File #################")
    # log_file = "merged_net_tune_record.json"
    # tvmc.tune(model, target="llvm -device=arm_cpu -mtriple=aarch64-linux-gnu", enable_autoscheduler = True, tuning_records=log_file)


    #Step 2: Compile
    # target = 'llvm'
    # package = tvmc.compile(model, target="llvm -device=arm_cpu -mtriple=aarch64-linux-gnu",cross='aarch64-linux-gnu-gcc',package_path="panda_controller.tar") #Step 2: Compile
    package_tuned = tvmc.compile(model, target="cuda -arch=sm_87",target_host='llvm -mtriple=aarch64-linux-gnu',cross='/home/qjz/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-gcc',package_path="oghr_controller.tar")
    print("################# Network Converted #################")
    # package_tuned = tvmc.compile(model, target="llvm -device=arm_cpu -mtriple=aarch64-none-linux-gnu",cross='aarch64-none-linux-gnu-gcc', tuning_records = log_file, package_path="panda_controller.tar")
    # print(tvm.target.Target.list_kinds())

    #Step 3: Run
    # result = tvmc.run(package, device="cpu")
    # print(result)
    # package_tuned = tvmc.TVMCPackage(package_path="panda_controller.tar")
    # result_tuned = tvmc.run(package_tuned, device="cpu")
    # print(result_tuned)

    # o_ex = np.zeros((1,1,208)).astype(np.float32)
    # o_pt = np.zeros((1, 1, 154)).astype(np.float32)
    # h_t = np.zeros((2, 1, 50)).astype(np.float32)
    # shape_dict = {'robot_state':o_pt.shape,'vision_input':o_ex.shape,'hidden_state':h_t.shape}
