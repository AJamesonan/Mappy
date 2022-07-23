var arr = [3,2,1,5,4,7,6]
function bubble_sort(arr) {
    var temp = 0
    for(var i =0;i<arr.length;i++){
        if( arr[i-1]== arr[i]){
          temp = arr[i]
          arr[i-1] = arr[i]
          arr[i] = temp
      }
      else {
        continue
      }
    }
  return arr

  }

console.log(bubble_sort(arr))