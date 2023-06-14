import torch

# # Check if CUDA is available
# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     print("CUDA is available")
# else:
#     device = torch.device("cpu")
#     print("CUDA is not available")

# # Create a tensor and move it to the selected device
# x = torch.tensor([1.0, 2.0, 3.0]).to(device)

# # Perform a simple operation
# y = x * 2

# # Move the result back to the CPU if CUDA is used
# if device.type == "cuda":
#     y = y.to("cpu")

# # Print the result
# print(y)
    
z = torch.tensor([[1.0, 2.0], [3.0, 2.1]])
print(z)
print(z.ndim)
print(z.shape)
