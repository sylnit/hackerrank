<?php

function rotateLeft($d, $arr)
{
    // Write your code here
    $len = count($arr);
    $rotations = ($d > $len ? ($len % $d) + 1 : $d);
    $rotated = array_slice($arr, 0, $rotations);
    $suffix_array = array_slice($arr, $rotations);
    return array_merge($suffix_array, $rotated);
}

print_r([1,2,3,4,5], 3);
