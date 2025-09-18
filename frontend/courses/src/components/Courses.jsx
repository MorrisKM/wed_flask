import { useState, useEffect } from 'react'
import Course from './Course'

const Courses = () => {
  const [courses, setCourse] = useState([])
  useEffect(()=> {
    async function fetchData(){
      let fetched_data = await fetch('http://127.0.0.1:5005/course/courses')
      let data = await fetched_data.json()
      console.log(data)
      setCourse(data)
    }
    fetchData()
  }, [])
  return (
    <div className='w-4/10 self-center justify-self-center'>
      <h1 className='text-center text-2xl'>Courses</h1>
      {courses.map(data => (
        <Course key={data.id} data={data} />
      ))}
    </div>
  )
}

export default Courses