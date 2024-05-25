import React, { Component } from 'react';
import VendorCard from './VendorCard';

export default class Vendors extends Component {
  constructor() {
    super();
    this.state = {
      articles: [],
      loading: false,
      error: null,
    };
  }

  async componentDidMount() {
    this.setState({ loading: true });
    try {
      const response = await fetch("http://192.168.1.9:8000/api/vendors/");
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const parsedData = await response.json();
      this.setState({ articles: parsedData, loading: false });
    } catch (error) {
      console.error("Error fetching data: ", error);
      this.setState({ error: error.message, loading: false });
    }
  }

  render() {
    const { articles, loading, error } = this.state;

    return (
      <div className="container my-3">
        <h2>Vendors List</h2>

        {loading && <p>Loading...</p>}
        {error && <p>Error: {error}</p>}

        <div className="row">
          {articles.map((element) => (
            <div className="col-md-3" key={element.url}>
              <VendorCard
                title={element.name ? element.name.slice(0, 45) : ""}
                address={element.address ? element.address.slice(0, 88) : ""}
                contact_details={element.contact_details ? element.contact_details.slice(0, 88) : ""}
                quality_rating_avg={element.quality_rating_avg ? element.quality_rating_avg: 0}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }
}