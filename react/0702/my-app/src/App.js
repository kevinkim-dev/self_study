import React, {Component} from 'react';
import Items from "./components/Items"
import Content from "./components/Content"
import Subject from "./components/Subject"
// import Clock from "./components/Clock"
import './App.css';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: 'read',
      selected_content_id:2,
      subject: {title: 'WEB', sub: 'World Wide Web'},
      welcome:{title: 'Welcome', desc: 'Hello, React!!'},
      contents: [
        {id:1, title:'HTML', desc: 'HTML is for information'},
        {id:2, title:'CSS', desc: 'CSS is for design'},
        {id:3, title:'JavaScript', desc: 'JavaScript is for interactive'},
      ]
    }
  }
  render() {
    var _title, _desc = null;
    if(this.state.mode === 'welcome'){
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if(this.state.mode === 'read'){
      var i = 0;
      while(i < this.state.contents.length){
        var data = this.state.contents[i];
        if(data.id === this.state.selected_content_id) {
          _title = data.title;
          _desc = data.title;
        }
        i = i+ 1
      }
    }
    return (
      <div className="App">
        {/* <Clock></Clock> */}
        <Subject
          title={this.state.subject.title} 
          sub={this.state.subject.sub}
          onChangePage={function(){
            this.setState({mode:'welcome'})
          }.bind(this)}
        >
        </Subject>
        <Items 
          onChangePage={function(id){
            this.setState({
              mode: 'read',
              selected_content_id:Number(id)
            })
          }.bind(this)}
          data={this.state.contents}
        ></Items>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}

export default App;
