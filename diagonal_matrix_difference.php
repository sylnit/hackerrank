<?php
/**
 * Given a square matrix, calculate the absolute difference between the sums of its diagonals.
 * For example, the square matrix  is shown below:
 * 1 2 3
 * 4 5 6
 * 9 8 9
 * The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
 *
 * Function description
 * Complete the  function in the editor below.
 * diagonalDifference takes the following parameter:
 * int arr[n][m]: an array of integers
 *
 * Return
 * int: the absolute diagonal difference
 */

function diagonalDifference($arr)
{
    // Write your code here
    $left = [];
    $right = [];
    $len = count($arr);
    $j=$len-1;
    for ($i=0; $i < $len; $i++) {
        $left[] = $arr[$i][$i];
        $right[] = $arr[$i][$j];
        $j -= 1;
    }
    return abs(array_sum($left)-array_sum($right));
}
