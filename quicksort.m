

function A = QuickSort (A, left, right) 

    if left < right
	[A, pvt] = PartitionPvt(A, left, right);
	A = QuickSort(A, left, pvt - 1);
	A = QuickSort(A, pvt + 1, right);
end

function [SortedSubArray, pivot] = PartitionPvt(SubArray, leftIndex, rightIndex)

	S = SubArray;
	left = leftIndex;
	right = rightIndex;

	P = S(left);
	i = left + 1;
	
	for j = i : right
		if S(j) < P
			temp1 = S(j);
			temp2 = S(i);
			S(j) = temp2;
			S(i) = temp1;
			i = i + 1;
		end
	end

	swap1 = S(left);
	swap2 = S(i-1);
	S(left) = swap2;
	S(i-1 ) = swap1;

	sortedArray = S;
	pivot = i;
	
