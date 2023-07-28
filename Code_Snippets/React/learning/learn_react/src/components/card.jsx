import {Grid} from 'react'

function Card() {
  return (
        <div className="card" style={{width: "18rem", textAlign: "center"}}>
            <img className="card-img-top" src="https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2021/08/learn-coding-online-for-free.webp" />
            <div className="card-body">
                <h5 className="card-title">Card title</h5>
                <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" className="btn btn-primary">Go somewhere</a>
            </div>
        </div>
  )
}

export default Card