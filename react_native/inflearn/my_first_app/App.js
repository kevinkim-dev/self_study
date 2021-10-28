import React, { Component } from 'react';
import {View, Text, StyleSheet, ScrollView, Button, TextInput, ActivityIndicator, Image} from 'react-native'
import Header from './src/header'
import Generator from './src/generator'
import NumList from './src/numlist'
import Input from './src/input'
import Picker from './src/picker'
import UFO from './assets/images/ufo.png'


class App extends Component {
  state = {
    myTextInput: '',
    alphabet: ['a', 'b', 'c', 'd']
  }


  onChangeInput = (event) => {
    this.setState({
      myTextInput: event
    })
  }

  onAddTextInput = () => {
    this.setState(prevState=> {
      return {
        myTextInput: '',
        alphabet: [...prevState.alphabet, prevState.myTextInput]
      }
    })
  }

  render() {
    return (
      <View style={styles.mainView}>
        <ActivityIndicator
          size="large"
          color="red"
          animating={true}
        />
        <Image 
          style={styles.image}
          source={{uri: 'https://picsum.photos/seed/picsum/200/300'}}
          resizeMode="contain"
          onLoadEnd={()=>alert('Image Loaded')}
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
  },
  input: {
    backgroundColor: '#cdcdcd',
    width: '100%',
    marginTop: 20,
    fontSize: 25,
    padding: 10
  },
  image: {
    width: '100%',
    height: 700
  }
})


export default App;
