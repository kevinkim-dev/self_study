import React, { Component } from 'react';
import {View, Text, StyleSheet, ScrollView, Button} from 'react-native'
import Header from './src/header'
import Generator from './src/generator'
import NumList from './src/numlist'
import Input from './src/input'

class App extends Component {
  state = {
    appName: 'My First App',
    random: [36, 999]
  }

  onAddRandomNum = () => {
    const randomNum = Math.floor(Math.random()*100)+1
    this.setState(now => {
      return {
        random: [...now.random, randomNum]
      }
    })
  }

  onNumDelete = (position) => {
    const newArray = this.state.random.filter((num, index)=> {
      return position != index;
    })
    this.setState({ random: newArray})
  }

  onAddTextInput = () => {
    alert('I want to add')
  }

  render() {
    return (
      <View style={styles.mainView}>
        <Input />
        <Button 
          title="Add Text Input"
          onPress={this.onAddTextInput}
        />
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
    // justifyContent: 'center'
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
