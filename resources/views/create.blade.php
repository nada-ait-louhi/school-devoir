@extends('layout')

@section('content')
<h3>Add New Student</h3>

<form action="/students" method="POST" enctype="multipart/form-data">
    @csrf

    <p>Name: <br><input type="text" name="name" required></p>
    <p>Email: <br><input type="email" name="email" required></p>
    <p>Phone: <br><input type="text" name="phone"></p>
    <p>Section: <br><input type="text" name="section"></p>
    <p>Image: <br><input type="file" name="image"></p>

    <button type="submit">Add Student</button>
</form>

<br>
<a href="/students">Back to List</a>
@endsection