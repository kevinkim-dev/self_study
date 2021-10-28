import React from 'react';
import {View, Text, StyleSheet, TextInput} from 'react-native'

class Input extends React.Component {

  state = {
    myTextInput: 'asfdasdf'
  }

  onChangeInput = (event) => {
    this.setState({
      myTextInput: event
    })
  }

  render() {
    return (
      <View style={styles.mainView}>
        <TextInput
          value={this.state.myTextInput}
          style={styles.input}
          onChange={this.onChangeInput}
          multiline={true}
          maxLength={10}
          autoCapitalize={'none'}
          editable={false}
        />
      </View>
    )
  }
}

const styles = StyleSheet.create({
  mainView: {
    width: '100%'
  },
  input: {
    backgroundColor: '#cdcdcd',
    width: '100%',
    marginTop: 20,
    fontSize: 25,
    padding: 10
  }
})

export default Input;
