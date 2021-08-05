<?php

/**
 *
 */

function timeConversion($s)
{
    // Write your code here
    $suff = substr($s, -2);
    $timePart = substr($s, 0, strlen($s)-2);
    $explodedTime = explode(':', $timePart);
    if ($suff == 'AM' && $explodedTime[0] < 12) {
        return $timePart;
    } elseif ($suff == 'AM' && $explodedTime[0] == 12) {
        $explodedTime[0] = '00';
        return implode(':', $explodedTime);
    } else {
        $explodedTime[0] += 12;
        return implode(':', $explodedTime);
    }
}

timeConversion('07:05:45PM');
