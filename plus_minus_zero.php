<?php

/**
 * Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
 *
 * Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
 *
 * Example
 * There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
 * 0.400000
 * 0.400000
 * 0.200000
 *
 * Function Description
 * Complete the plusMinus function in the editor below.
 * plusMinus has the following parameter(s):
 * int arr[n]: an array of integers
 * Print
 * Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
 */

function plusMinus($arr)
{
    // Write your code here
    $denominator = count($arr);
    $pos = 0;
    $neg = 0;
    $zero = 0;
    for ($i = 0; $i < $denominator; $i++) {
        if ($arr[$i] == 0) {
            $zero += 1;
        } elseif ($arr[$i] > 0) {
            $pos += 1;
        } elseif ($arr[$i] < 0) {
            $neg += 1;
        }
    }
    echo number_format($pos/$denominator, 6)."\r\n";
    echo number_format($neg/$denominator, 6)."\r\n";
    echo number_format($zero/$denominator, 6)."\r\n";
}
