import React, {Component} from 'react';


class Clock extends Component {
  render() {
    return (
      <clock>
        {new Date().toLocaleTimeString()}
      </clock>
    )
  }
}

export default Clock;