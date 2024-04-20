from mmpose.apis import MMPoseInferencer


# 使用模型别名创建推理器
inferencer = MMPoseInferencer(pose3d="human3d")


folder_path = 0

result_generator = inferencer(folder_path, show=True, use_oks_tracking=True)
results = [result for result in result_generator]
pred_instances = results[0].pred_instances

print(pred_instances.keypoints)