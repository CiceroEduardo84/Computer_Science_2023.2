from sbbst import sbbst 

if __name__=="__main__":
    tree = sbbst()
    nums = [131, 4, 134, 135, 180, 1, 3, 21, 14, 142, 80, 146]
    for num in nums:
        tree.insert(num)

    print("Número de elementos:", tree.getSize())
    print("altura:", tree.getHeightTree())
    print("Min valor:", tree.getMinVal())
    print("Max valor:", tree.getMaxVal())
    print("3º menor valor:", tree.kthsmallest(3))
    print("2º maior valor:", tree.kthlargest(2))
    print("Pre-Orden:", tree.preOrder())
