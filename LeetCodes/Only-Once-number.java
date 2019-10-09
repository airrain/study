public class Only-Once-number(){
	public getNumber(){
nums = [2,4,5,4,2,5,6]

int ans = nums[0];
if(nums.length > 1){
	for(int i = 1;i < nums.length;i++){
		ans = ans ^ nums[i];
	}
}
return ans;
}
System.out,println(ans)
}
