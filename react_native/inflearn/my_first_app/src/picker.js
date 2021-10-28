import React from 'react';
import {View, Text, StyleSheet} from 'react-native'

class PickerComponent extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        {/* <Picker
          style={{height: 50, width: 250}}
        >

        </Picker> */}
      </View>

    )
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 20,
    marginBottom: 200,
    alignItems: 'center'
  }
})

export default PickerComponent;
