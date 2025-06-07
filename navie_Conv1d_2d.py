
def Conv1d(input,kernel,stride):
  output_len = ((len(input)-len(kernel))//stride)+1
  op_list = []
  for i in range(output_len):
    kernel_pos = i*stride
    res=0
    for j in range(len(K)):
      res+=A[kernel_pos+j]*K[j]
    op_list.append(res)
  return op_list

def Conv2d(input,kernel,stride):
   rows = len(input)
   columns = len(input[0])

   kernel_row = len(kernel)
   kernel_col = len(kernel[0])

   out_height = ((rows-kernel_row)//stride[0])+1
   out_width =  ((columns-kernel_col)//stride[1])+1

   out_put = [[0 for i in range(out_width)] for j in range(out_height)]

   for i in range(0,out_height):
     for j in range(0,out_width):
       row = i*stride[0]
       col = j*stride[1]
       res = 0
       for ki in range(kernel_row):
         for kj in range(kernel_col):
          res+=input[row+ki][col+kj]*kernel[ki][kj]
       out_put[i][j] = res
   return out_put


if __name__ == "__main__":
  ######### conv2d operation check #################
  ipl=[[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5]]
  kernel=[[1,2,3],[1,2,3],[1,2,3]]
  conv_out = Conv2d(ipl,kernel,stride=[1,1])
  print(conv_out)
  #######  conv1d operation check ####################
  A=[1,2,3,4,5,6,7,8]
  K=[1,2,3]
  output= Conv1d(A,K,2)
  print(output)
