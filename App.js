import React, { Component } from 'react';
class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      query: "", // my query
      artist: null  // my response.
    }
  }

  search() {
    console.log('this.state', this.state);
    const BASE_URL = 'https://api.spotify.com/v1/search?';
    const FETCH_URL = BASE_URL + 'q=' + this.state.query + '&type=artist&limit=1';
    var accessToken = 'BQAECW-WWVHBWaMc3yVE21pnl9Nf268emgEJLGFLPm905O06KXM5giILuRXqDAIQ3lJp34YJyAuQDDzWnZjgkhqoNw1q-aMsYo9ymIg00zDDPxf4P4nUDgEVxzim2AtbcodO7fLQ4n0HEc9-R-l2ECs9S_yY7gSpm9_9ImJusYmW9Be6Hg&refresh_token=AQCG8q1fcy1ayc1jrOzmLIQepVzMr7XcRBNqgW_q9CieLHCfPnawre5CwHDD_gke-J6_s-Cle1MmMPa2MenOqj0eS8-PK674-mm69vswipbr3EptmAfYmONTLcmykRcywTM'

    var myOptions = {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + accessToken
      },
      mode: 'cors',
      cache: 'default'
    };

    fetch(FETCH_URL, myOptions)
      .then(response => response.json())
      .then(json => {
        const artist = json.artists.items[0];
        this.setState({ artist });
      })

  }

  render() {

    let artist = {
      name: '',
      followers: {
        total: ''
      }
    };
    if (this.state.artist !== null) {
      artist = this.state.artist;
    }

    return (
      // return JSX
      <div className="container">
        <hr />
        <div className="col-lg-6">
          <div className="input-group">
            <input type="text"
              onChange={event => { this.setState({ query: event.target.value }) }}
            className="form-control" placeholder="Search for..." />
            <span className="input-group-btn">
              <button
              onClick={()=> this.search()}
               className="btn btn-default" type="button">Go!</button>
            </span>
          </div>
        </div>
        <hr />
        <div>
          <div> {artist.name}   </div>
          <div> {artist.followers.total} </div>
        </div>


        </div>
    )
  }
}
export default App;