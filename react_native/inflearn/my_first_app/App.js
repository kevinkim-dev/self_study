import React, { Component } from 'react';
import {View, Text, StyleSheet} from 'react-native'
import Header from './src/header'


class App extends Component {
  state = {
    appName: 'My First App'
  }

  render() {
    return (
      <View style={styles.mainView}>
        {/* <Header name={this.state.appName} /> */}
        <Text onPress={()=>alert('hello world!')}>Hello World!</Text>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  mainView: {
    flex: 1,
    backgroundColor: 'white',
    paddingTop: 50,
    alignItems: 'center',
    justifyContent: 'center'
  },
  subView: {
    backgroundColor: 'yellow',
    marginBottom: 10
  },
  mainText: {
    fontSize: 20,
    fontWeight: 'normal',
    color: 'red',
    padding: 20
  }
})


export default App;
