import { useEffect, useState } from 'react'
import Coils from './components/Coils'
import './App.css'

function App() {
  const [coils , setcoils] = useState([])

  useEffect(() => {
    fetcher()
  }, [])

  const fetcher = async () => {
    const URI = 'http://localhost:5000/coils'
    const responce = await fetch(URI)
    const data = await responce.json()
    setcoils(data)
    console.log(coils, data)
  }

  return (
    <>
      <h1>Coils</h1>
      <table>
        <Coils coils={coils} />
      </table>
    </>
  )
}

export default App
