import Rating from './Rating'
import React, { Component } from 'react'


export default class VendorCard extends Component {
  render() {
    let {title, contact_details, address, 
        vendor_code, on_time_delivery_rate,
        quality_rating_avg, average_response_time,
        fulfillment_rate
    } = this.props;
    return (
        <div className='container my-3'>
        <div className="card" style={{width: "18rem"}}>
          <img src="vendor.png" className="card-img-top" alt="..." style={{width:"100%", height: "200px"}} />
          <div className="card-body">
            <h5 className="card-title">{title} </h5>
            <a className="card-text" href="{contact_details}">{contact_details}</a>
            <p className="card-text">{address}</p>
            <Rating quality_rating_avg={quality_rating_avg} />
          </div>
        </div>
      </div>
    )
  }
}
