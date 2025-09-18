import React from 'react'

const Course = ({data}) => {
  return (
    <div className='mb-4 p-2 border-1'>
      <p>course name: {data.name}</p>
      <p>course description: {data.description}</p>
      <p>course credits: {data.credits}</p>
    </div>
  )
}

export default Course