@extends('layout')

@section('content')
<h2>Edit Student</h2>

<form action="/students/{{ $student->id }}" method="POST" enctype="multipart/form-data">
    @csrf
    @method('PUT')

    <div class="mb-3">
        <label>Name</label>
        <input type="text" name="name" class="form-control" value="{{ $student->name }}" required>
    </div>

    <div class="mb-3">
        <label>Email</label>
        <input type="email" name="email" class="form-control" value="{{ $student->email }}" required>
    </div>

    <div class="mb-3">
        <label>Phone</label>
        <input type="text" name="phone" class="form-control" value="{{ $student->phone }}" required>
    </div>

    <div class="mb-3">
        <label>Section</label>
        <input type="text" name="section" class="form-control" value="{{ $student->section }}" required>
    </div>

    <div class="mb-3">
        <label>Image</label>
        <input type="file" name="image" class="form-control">
    </div>

    <button type="submit" class="btn btn-primary">Update Student</button>
    <a href="/students" class="btn btn-secondary">Back</a>
</form>
@endsection