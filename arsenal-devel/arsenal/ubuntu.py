#!/usr/bin/env python
#

# Warning - using the following dictionary to get the series name from
# the kernel version works for the linux package, but not for some
# others (some ARM packages are known to be wrong). This is because the
# ARM kernels used for some series are not the same as the main kernels
#

series = [
    "hardy",
    "jaunty",
    "karmic",
    "lucid",
    "maverick",
    "natty",
    "oneiric",
    "precise",
    "quantal",
    ]

importances = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "Wishlist",
    "Undecided",
    "Unknown",
    ]

status = [
    "New",
    "Incomplete",
    "Confirmed",
    "Triaged",
    "In Progress",
    "Fix Committed",
    "Fix Released",
    "Invalid",
    "Won't Fix",
    "Opinion",
    "Expired",
    "Unknown",
    ]


# UbuntuError
#
class UbuntuError(Exception):
    # __init__
    #
    def __init__(self, error):
        self.msg = error

# Ubuntu
#
class Ubuntu:

    db = {
        '12.10' :
        {
            'development' : True,   # This is the version that is currently under development
            'series_version' : '12.10',
            'kernel'    : '3.4.0',
            'name'      : 'quantal',
            'supported' : True,
            # adjust packages when this goes live
            'packages'  :
            [
                'linux',
                'linux-meta',
                'linux-ti-omap4',
                'linux-meta-ti-omap4'
            ],
            'dependent-packages' :
            {
                'linux' : { 'meta' : 'linux-meta' },
                'linux-ti-omap4' : { 'meta' : 'linux-meta-ti-omap4' }
            },
            'derivative-packages' :
            {
                'linux' : [ 'linux-ti-omap4' ]
            },
            'sha1' : '',
            'md5' : ''
        },
        '12.04' :
        {
            'development' : False,
            'series_version' : '12.04',
            'kernel'    : '3.2.0',
            'name'      : 'precise',
            'supported' : True,
            # adjust packages when this goes live
            'packages'  :
            [
                'linux',
                'linux-meta',
                'linux-ti-omap4',
                'linux-meta-ti-omap4'
            ],
            'dependent-packages' :
            {
                'linux' : { 'meta' : 'linux-meta' },
                'linux-ti-omap4' : { 'meta' : 'linux-meta-ti-omap4' }
            },
            'derivative-packages' :
            {
                'linux' : [ 'linux-ti-omap4' ]
            },
            'sha1' : '',
            'md5' : ''
        },
        '11.10' :
        {
            'series_version' : '11.10',
            'kernel'    : '3.0.0',
            'name'      : 'oneiric',
            'supported' : True,
            # adjust packages when this goes live
            'packages'  :
            [
                'linux',
                'linux-meta',
                'linux-ti-omap4',
                'linux-meta-ti-omap4'
            ],
            'dependent-packages' :
            {
                'linux' : { 
                    'meta' : 'linux-meta',
                    'lbm'  : 'linux-backports-modules-3.0.0'
                },
                'linux-ti-omap4' : { 'meta' : 'linux-meta-ti-omap4' }
            },
            'derivative-packages' :
            {
                'linux' : [ 'linux-ti-omap4' ]
            },
            'sha1' : '',
            'md5' : ''
        },
        '11.04' :
        {
            'series_version' : '11.04',
            'kernel'    : '2.6.38',
            'name'      : 'natty',
            'supported' : True,
            'packages'  :
            [
                'linux',
                'linux-meta',
                'linux-ti-omap4',
                'linux-meta-ti-omap4',
                'linux-backports-modules-2.6.38'
            ],
            'dependent-packages' :
            {
                'linux' : {
                    'meta' : 'linux-meta',
                    'lbm'  : 'linux-backports-modules-2.6.38'
                },
                'linux-ti-omap4' : { 'meta' : 'linux-meta-ti-omap4' }
            },
            'derivative-packages' :
            {
                'linux' : [ 'linux-ti-omap4' ]
            },
            'sha1' : '0770b9d2483eaeee4b80aec1fd448586b882003e',
            'md5' : 'cf0b587742611328f095da4b329e9fc7'
        },
        '10.10' :
        {
            'series_version' : '10.10',
            'kernel' : '2.6.35',
            'name' : 'maverick',
            'supported' : True,
            'packages' :
            [
                'linux',
                'linux-ti-omap4',
                'linux-mvl-dove',
                'linux-meta',
                'linux-ports-meta',
                'linux-meta-mvl-dove',
                'linux-meta-ti-omap4',
                'linux-backports-modules-2.6.35'
            ],
            'dependent-packages' :
            {
                'linux' : {
                    'meta' : 'linux-meta',
                    'ports-meta' : 'linux-ports-meta',
                    'lbm': 'linux-backports-modules-2.6.35'
                },
                'linux-ti-omap4' : { 'meta' : 'linux-meta-ti-omap4' },
                'linux-mvl-dove' : { 'meta' :  'linux-meta-mvl-dove' }
            },
            'derivative-packages' :
            {
                'linux' : [ 'linux-ti-omap4', 'linux-mvl-dove' ]
            },
            'sha1' : 'a2422f9281766ffe2f615903712819b9b0d9dd52',
            'md5' : '62001687bd94d1c0dd9a3654c64257d6'
        },
        '10.04' :
        {
            'series_version' : '10.04',
            'kernel' : '2.6.32',
            'name' : 'lucid',
            'supported' : True,
            'packages' :
            [
                'linux',
                'linux-fsl-imx51',
                'linux-mvl-dove',
                'linux-ec2',
                'linux-meta',
                'linux-ports-meta',
                'linux-meta-ec2',
                'linux-meta-mvl-dove',
                'linux-meta-fsl-imx51',
                'linux-backports-modules-2.6.32',
                #'linux-lts-backport-oneiric',
                #'linux-meta-lts-backport-oneiric',
                'linux-lts-backport-natty',
                'linux-meta-lts-backport-natty',
                'linux-lts-backport-maverick',
                'linux-meta-lts-backport-maverick'
            ],
            'dependent-packages' :
            {
                'linux' : {
                    'meta' : 'linux-meta',
                    'ports-meta' : 'linux-ports-meta',
                    'lbm' : 'linux-backports-modules-2.6.32'
                },
                'linux-fsl-imx51' : { 'meta' : 'linux-meta-fsl-imx51' },
                'linux-ec2' : { 'meta' : 'linux-meta-ec2' },
                'linux-lts-backport-oneiric' : {
                    'meta' : 'linux-meta-lts-backport-oneiric'
                },
                'linux-lts-backport-natty' : {
                    'meta' : 'linux-meta-lts-backport-natty'
                },
                'linux-lts-backport-maverick' : {
                    'meta' : 'linux-meta-lts-backport-maverick'
                }
            },
            'derivative-packages' :
            {
                'linux' : [ 'linux-fsl-imx51', 'linux-ec2' ]
            },
            'backport-packages' :
            {
                'linux-lts-backport-oneiric' : [ 'linux', '11.10' ],
                'linux-lts-backport-natty' : [ 'linux', '11.04' ],
                'linux-lts-backport-maverick' : [ 'linux', '10.10' ],
            },
            'sha1' : '298cbfdb55fc64d1135f06b3bed3c8748123c183',
            'md5' : '4b1f6f6fac43a23e783079db589fc7e2'
        },
        '9.10' :
        {
            'series_version' : '9.10',
            'kernel' : '2.6.31',
            'name' : 'karmic',
            'supported' : False,
            'packages' :
            [
                'linux',
                'linux-fsl-imx51',
                'linux-mvl-dove',
                'linux-ec2',
                'linux-meta',
                'linux-ports-meta',
                'linux-meta-ec2',
                'linux-meta-mvl-dove',
                'linux-meta-fsl-imx51',
                'linux-backports-modules-2.6.31'
            ],
            'sha1' : '6b19c2987b0e2d74dcdca2aadebd5081bc143b72',
            'md5' : '16c0355d3612806ef87addf7c9f8c9f9'
        },
        '9.04' :
        {
            'series_version' : '9.04',
            'kernel' : '2.6.28',
            'name' : 'jaunty',
            'supported' : False,
            'packages' : [],
            'sha1' : '92d6a293200566646fbb9215e0633b4b9312ad38',
            'md5' : '062c29b626a55f09a65532538a6184d4'
        },
        '8.10' :
        {
            'series_version' : '8.10',
            'kernel' : '2.6.27',
            'name' : 'intrepid',
            'supported' : False,
            'packages' : []
        },
        '8.04' :
        {
            'series_version' : '8.04',
            'kernel' : '2.6.24',
            'name' : 'hardy',
            'supported' : True,
            'packages' :
            [
                'linux',
                'linux-meta',
                'linux-backports-modules-2.6.24',
                'linux-ubuntu-modules-2.6.24',
                'linux-restricted-modules-2.6.24'
            ],
            'dependent-packages' :
            {
                'linux' : {
                    'meta' : 'linux-meta',
                    'lbm' : 'linux-backports-modules-2.6.24',
                    'lrm' : 'linux-restricted-modules-2.6.24',
                    'lum' : 'linux-ubuntu-modules-2.6.24'
                }
            },
            'sha1' : 'ccccdc4759fd780a028000a1b7b15dbd9c60363b',
            'md5' : 'e4aad2f8c445505cbbfa92864f5941ab'
        },
        '7.10' :
        {
            'series_version' : '7.10',
            'kernel' : '2.6.22',
            'name' : 'gutsy',
            'supported' : False,
            'packages' : []
        },
        '7.04' :
        {
            'series_version' : '7.04',
            'kernel' : '2.6.20',
            'name' : 'feisty',
            'supported' : False,
            'packages' : []
        },
        '6.06' :
        {
            'series_version' : '6.06',
            'kernel' : '2.6.15',
            'name' : 'dapper',
            'supported' : False,
            'packages' :
            [
                'linux-source-2.6.15',
                'linux-backports-modules-2.6.15',
                'linux-restricted-modules-2.6.15'
            ]
        },
    }

    index_by_kernel_version = {
        '3.2.0'    : db['12.04'],
        '3.0.0'    : db['11.10'],
        '2.6.38'   : db['11.04'],
        '2.6.35'   : db['10.10'],
        '2.6.32'   : db['10.04'],
        '2.6.31'   : db['9.10'],
        '2.6.28'   : db['9.04'],
        '2.6.27'   : db['8.10'],
        '2.6.24'   : db['8.04'],
        '2.6.22'   : db['7.10'],
        '2.6.20'   : db['7.04'],
        '2.6.15'   : db['6.06'],
    }

    index_by_series_name = {
        'precise'  : db['12.04'],
        'oneiric'  : db['11.10'],
        'natty'    : db['11.04'],
        'maverick' : db['10.10'],
        'lucid'    : db['10.04'],
        'karmic'   : db['9.10'],
        'jaunty'   : db['9.04'],
        'intrepid' : db['8.10'],
        'hardy'    : db['8.04'],
        'gutsy'    : db['7.10'],
        'feisty'   : db['7.04'],
        'dapper'   : db['6.06'],
    }

    kernel_source_packages = [
        'linux',
        'linux-ti-omap4', # maverick, natty
        'linux-mvl-dove', # maverick, karmic, lucid
        'linux-fsl-imx51', # karmic, lucid
        'linux-ec2',
        'linux-meta',
        'linux-meta-ec2',
        'linux-meta-mvl-dove', # maverick, karmic, lucid
        'linux-meta-ti-omap4', # maverick, natty
        'linux-meta-fsl-imx51', # karmic, lucid ?
        'linux-ports-meta',
        'linux-source-2.6.15',

        'linux-backports-modules-2.6.15',
        'linux-backports-modules-2.6.24',
        'linux-backports-modules-2.6.31',
        'linux-backports-modules-2.6.32',
        'linux-backports-modules-2.6.35',
        'linux-backports-modules-2.6.38',
        'linux-backports-modules-3.0.0',

        'linux-restricted-modules-2.6.15',
        'linux-restricted-modules-2.6.24',

        'linux-ubuntu-modules-2.6.24',

        'linux-lts-backport-maverick',
        'linux-lts-backport-natty',
        #'linux-lts-backport-oneiric',
        'linux-meta-lts-backport-maverick',
        'linux-meta-lts-backport-natty',
        #'linux-meta-lts-backport-oneiric',
    ]

    # lookup
    #
    def lookup(self, key):
        """
        Using the given key, find the matching record in the db and return that record.
        Note, the key argument can be a series-name, series-version or a kernel-version.
        """
        if key in Ubuntu.db:
            record = Ubuntu.db[key]
        elif key in Ubuntu.index_by_kernel_version:
            record = Ubuntu.index_by_kernel_version[key]
        elif key in Ubuntu.index_by_series_name:
            record = Ubuntu.index_by_series_name[key]
        else:
            raise KeyError(key)

        return record

    # is_development_series
    #
    def is_development_series(self, series):
        '''
        Returns True if the series passed in is the current series under development.
        '''
        try:
            retval = self.db['series']['development']
        except KeyError:
            retval = False
        return retval

    # is_supported_series
    #
    def is_supported_series(self, series):
        """
        Lookup the given series and return whether it is still supported or not. Note, since
        this uses the 'lookup' method, the series argument can be a series-name, series-version
        or a kernel-version.
        """
        retval = False

        rec = self.lookup(series)
        retval = rec['supported']

        return retval

    # supported_series
    #
    @property
    def supported_series(self):
        """
        A list of all the currently supported series names.
        """
        retval = []
        for series in self.db:
            if self.db[series]['supported']:
                retval.append(self.db[series]['name'])

        return retval

    # active_packages
    #
    @property
    def active_packages(self):
        """
        A list of all the packages for all the supported series.
        """
        retval = []
        for series in self.db:
            if self.db[series]['supported']:
                for pkg in self.db[series]['packages']:
                    if pkg not in retval:
                        retval.append(pkg)

        return retval

    # series where that package-version is found
    #
    def series_name(self, package, version):
        """
        Return the series name where that package-version is found
        """
        if (package == 'linux' or
            package == 'linux-ti-omap4' or
            package == 'linux-ec2'):
            for entry in self.db.itervalues():
                if version.startswith(entry['kernel']):
                    return entry['name']
        if package.startswith('linux-lts-backport'):
            for entry in self.db.itervalues():
                if entry['name'] in version:
                    return entry['name']
        if package == 'linux-mvl-dove' or package == 'linux-fsl-imx51':
            version, release = version.split('-')
            if release:
                abi, upload = release.split('.')
                try:
                    abi_n = int(abi)
                except ValueError:
                    abi_n = 0
                if abi_n:
                    if package == 'linux-mvl-dove':
                        if abi_n < 400:
                            return 'lucid'
                        else:
                            return 'maverick'
                    if package == 'linux-fsl-imx51':
                        if abi_n < 600:
                            return 'karmic'
                        else:
                            return 'lucid'
        return None

if __name__ == '__main__':
    ubuntu = Ubuntu()
    db = ubuntu.db

    #for record in db:
    #    print(db[record])

    print(ubuntu.lookup('2.6.32'))
    print(ubuntu.lookup('lucid'))
    print(ubuntu.lookup('10.04'))

# vi:set ts=4 sw=4 expandtab:
