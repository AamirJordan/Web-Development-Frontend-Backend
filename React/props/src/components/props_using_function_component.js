import React from 'react'


const Hii = (props) => {  //  OR    const Hii = {name, heroname} => {
    const {name, heroname} = props
    return (
        <div>
          <h1> Hello {name} a.k.a {heroname} </h1>

        </div>

    )

}

export default Hii
