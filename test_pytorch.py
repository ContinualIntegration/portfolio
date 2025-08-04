# This was produced by a Google search in an AI overview result on Aug 4 2025.
# It was slightly modified.
# It has a non-deterministic test of Tensor operations as they require a parameter
# to specify CUDA or regular CPU architecture.

import torch

def test_pytorch():
    """
    Tests the PyTorch installation, including CUDA availability and a basic tensor operation.
    """
    print("--- PyTorch Installation Test ---")

    # 1. Check PyTorch version
    print(f"PyTorch version: {torch.__version__}")

    # 2. Check CUDA availability
    if torch.cuda.is_available():
        print("CUDA is available! PyTorch can use your GPU.")
        print(f"CUDA version: {torch.version.cuda}")
        print(f"Number of GPUs: {torch.cuda.device_count()}")
        print(f"Current GPU name: {torch.cuda.get_device_name(0)}")
        device = torch.device("cuda:0")
    else:
        print("CUDA is NOT available. PyTorch will run on CPU.")
        device = torch.device("cpu")

    # 3. Perform a basic tensor operation
    print(f"\nPerforming a basic tensor operation on {device}...")
    try:
        x = torch.randn(4, 4, device=device)
        y = torch.randn(4, 4, device=device)
        z = x + y
        print(f"Tensor x:\n{x}")
        print(f"Tensor y:\n{y}")
        print(f"Tensor z (x + y):\n{z}")
        print("Basic tensor operation successful!")
    except Exception as e:
        print(f"Error during basic tensor operation: {e}")

    print("\n--- Test Complete ---")

if __name__ == "__main__":
    test_pytorch()
