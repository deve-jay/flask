import React from 'react'

const Coils = (coils) => {
  return (
    <div><thead>
        <th>name</th>
        <th>quantity</th>
        <th>orderrecived date</th>
        <th>wiregauge</th>
        <th>net weight</th>
        </thead>
        <tbody>
        {coils.coils.map((coil) => (
          <tr key={coil._id}>
            <td>{coil.name}</td>
            <td>{coil.quantity}</td>
            <td>{coil.orderreciveddate}</td>
            <td>{coil.wiregauge}</td>
            <td>{coil.netweight}</td>
          </tr>
        ))}
        </tbody>
        </div>
  )
}

export default Coils