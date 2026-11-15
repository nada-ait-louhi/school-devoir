@extends('layout')

@section('content')

<style>
.lbl {
    color: black;
    width: 200px;
    font-weight: bold;
    background-color: #efefef;
    border-radius: 5px;
    font-size: 16px;
    padding-left: 11px;
    padding-right: 4px;
    padding-bottom: 5px;
    margin-right: 100px;
    margin-bottom: 70px;
}
</style>

<h3> Student Details </h3>

<table style="border:0px;">
<tr>
<td>
    <p> <b class="lbl">ID : </b> {{$student->id}} </p>
    <p> <b class="lbl">Name : </b> {{$student->name}} </p>
    <p> <b class="lbl">Phone : </b> {{$student->phone}} </p>
    <p> <b class="lbl">Email : </b> {{$student->email}} </p>
    <p> <b class="lbl">Section : </b> {{$student->section}}</p>
</td>
<td style="padding-left:150px;">
    <img src="/image/{{$student->image}}" width="128" height="128">
</td>
</tr>
</table>

<br>
<a href="/students">Back to List</a>

@endsection